#! .venv/bin/python
import json
import uuid
from typing import TypedDict, List
import boto3
from boto3.dynamodb.types import TypeDeserializer
from botocore.exceptions import ClientError


TABLE_NAME = "Recipes"


class ServiceError(Exception):
    """
    Custom exception class for service errors.
    """

    def __init__(self, message, status_code: int, body: dict):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.body = body

    def __str__(self):
        return f"ServiceError: {self.message}"

    def client_return(self):
        return {
            "statusCode": self.status_code,
            "body": json.dumps(self.body),
        }


class RecipeRecord(TypedDict):
    id: str
    title: str
    description: str
    image: str
    source: str
    original_url: str
    makes: str
    active: str
    notes: str
    ingredients: list[str]
    instructions: list[str]
    tags: list[str]
    our_notes: str


class RecipeRecordAttributes(TypedDict):
    title: str
    description: str
    image: str
    source: str
    original_url: str
    makes: str
    active: str
    notes: str
    our_notes: str


class RecipeSummaryRecord(TypedDict):
    id: str
    title: str
    tags: list[str]


class Recipe:

    def __init__(self, record: RecipeRecord):
        self.id = record["id"] if "id" in record else str(uuid.uuid4())
        self.title = record["title"] if "title" in record else ""
        self.description = record["description"] if "description" in record else ""
        self.image = record["image"] if "image" in record else ""
        self.source = record["source"] if "source" in record else ""
        self.original_url = record["original_url"] if "original_url" in record else ""
        self.makes = record["makes"] if "makes" in record else ""
        self.active = record["active"] if "active" in record else ""
        self.notes = record["notes"] if "notes" in record else ""
        self.ingredients = record["ingredients"] if "ingredients" in record else []
        self.instructions = record["instructions"] if "instructions" in record else []
        self.tags = record["tags"] if "tags" in record else []
        self.our_notes = record["our_notes"] if "our_notes" in record else ""

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "source": self.source,
            "original_url": self.original_url,
            "makes": self.makes,
            "active": self.active,
            "notes": self.notes,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "tags": self.tags,
            "our_notes": self.our_notes,
        }

    def add_recipe(self):
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        try:
            table.put_item(Item=self.to_dict(), ConditionExpression="attribute_not_exists(id)")
            return self.to_dict()
        except ClientError as e:
            message = (
                f"Error putting item: key='{self.id}'\n" f"Error={e.response['Error']['Message']}"
            )
            print((message))
            raise ServiceError(message, 500, {"error": message})

    def update_recipe(self, new_record_attributes: RecipeRecordAttributes):
        """
        Update an item in the DynamoDB table.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        update_expression = "SET "
        expression_attribute_values = {}
        for key, value in new_record_attributes.items():
            if key == "id" or key == "ingredients" or key == "instructions" or key == "tags":
                # Skip updating these fields
                continue
            update_expression += f"{key} = :{key}, "
            expression_attribute_values[f":{key}"] = value
        if update_expression.endswith(", "):
            update_expression = update_expression[:-2]
        if update_expression == "SET ":
            return
        try:
            response = table.update_item(
                Key={"id": self.id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="ALL_NEW",
            )
            return response["Attributes"]
        except ClientError as e:
            message = (
                f"Updating item: key='{self.id}'\n"
                f"UpdateExpression='{update_expression}'\n"
                f"ExpressionAttributeValues='{json.dumps(expression_attribute_values, indent=2)}'\n"
                f"Error={e.response['Error']['Message']}"
            )
            print(message)
            raise ServiceError(message, 500, {"error": message})

    def delete_recipe(self):
        """
        Delete an item from the DynamoDB table.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        try:
            table.delete_item(Key={"id": self.id})
        except ClientError as e:
            message = (
                f"Error deleting item: key='{self.id}'\n" f"Error={e.response['Error']['Message']}"
            )
            print(message)
            raise ServiceError(message, 500, {"error": message})

    def add_list_item(self, list_name, new_value):
        """
        Add an item to a list in the DynamoDB table.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        update_expression = (
            f"SET {list_name} = list_append(if_not_exists({list_name}, :empty_list), :new_value)"
        )
        expression_attribute_values = {":new_value": [new_value], ":empty_list": []}
        try:
            response = table.update_item(
                Key={"id": self.id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="ALL_NEW",
            )
            return response["Attributes"]
        except ClientError as e:
            message = (
                f"Adding item to list: key='{self.id}'\n"
                f"UpdateExpression='{update_expression}'\n"
                f"ExpressionAttributeValues='{json.dumps(expression_attribute_values, indent=2)}'\n"
                f"Error={e.response['Error']['Message']}"
            )
            print(message)
            raise ServiceError(message, 500, {"error": message})

    def delete_list_item(self, list_name, index):
        """
        Delete an item from a list in the DynamoDB table.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        update_expression = f"REMOVE {list_name}[{index}]"
        try:
            response = table.update_item(
                Key={"id": self.id},
                UpdateExpression=update_expression,
                ReturnValues="ALL_NEW",
            )
            return response["Attributes"]
        except ClientError as e:
            message = (
                f"Error deleting item from list: key='{self.id}'\n"
                f"UpdateExpression='{update_expression}'\n"
                f"Error={e.response['Error']['Message']}"
            )
            print(message)
            raise ServiceError(message, 500, {"error": message})

    def update_list_item(self, list_name: str, index: int, new_value: str):
        """
        Update an item in a list in the DynamoDB table.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        update_expression = f"SET {list_name}[{index}] = :new_value"
        expression_attribute_values = {":new_value": new_value}
        try:
            response = table.update_item(
                Key={"id": self.id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="ALL_NEW",
            )
            return response["Attributes"]
        except ClientError as e:
            message = (
                f"Error updating item in list: key='{self.id}'\n"
                f"UpdateExpression='{update_expression}'\n"
                f"ExpressionAttributeValues='{json.dumps(expression_attribute_values, indent=2)}'\n"
                f"Error={e.response['Error']['Message']}"
            )
            print(message)
            raise ServiceError(message, 500, {"error": message})

    @staticmethod
    def get_recipe(recipe_id):
        client = boto3.client("dynamodb")
        try:
            response = client.get_item(
                TableName=TABLE_NAME,
                Key={"id": {"S": recipe_id}},
            )
        except ClientError as e:
            message = (
                f"Error getting item: key='{recipe_id}'\n" f"Error={e.response['Error']['Message']}"
            )
            print(message)
            raise ServiceError(message, 500, {"error": message})
        recipe = response.get("Item", None)
        if recipe is None:
            raise ServiceError(f"Recipe not found: {recipe_id}", 404, {"error": "Not found"})
        deserializer = TypeDeserializer()
        return Recipe({k: deserializer.deserialize(v) for k, v in recipe.items()})

    @staticmethod
    def get_all_recipes() -> list[RecipeSummaryRecord]:
        """
        Scan the DynamoDB table and retrieve all items.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        try:
            response = table.scan(ProjectionExpression="id, title, tags")
            items = response["Items"]

            # If there are more pages, continue scanning
            while "LastEvaluatedKey" in response:
                response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
                items.extend(response["Items"])
        except ClientError as e:
            message = f"Error scanning table: {e.response['Error']['Message']}"
            print(message)
            raise ServiceError(message, 500, {"error": message})
        return items

    @staticmethod
    def batch_write(recipes: List["Recipe"]):
        """
        Batch write items to DynamoDB.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(TABLE_NAME)
        try:
            with table.batch_writer() as batch:
                for recipe in recipes:
                    if not isinstance(recipe, Recipe):
                        raise ServiceError(
                            f"Invalid recipe type: {type(recipe)}",
                            500,
                            {"error": f"Invalid recipe type: {type(recipe)}"},
                        )
                    batch.put_item(Item=recipe.to_dict())
            return
        except ClientError as e:
            message = f"Error batch writing items: {e.response['Error']['Message']}"
            print(message)
            raise ServiceError(message, 500, {"error": message})


def get_path_param(event, path_parameter: str):
    """
    Get the recipe id from the event path parameters
    Parameters:
        event: Dict containing the Lambda function event data
    Returns:
        str: The recipe id
    """
    try:
        return event["pathParameters"][path_parameter]
    except KeyError:
        return None


def lambda_handler(event, context):
    """
    Main Lambda handler function
    Parameters:
        event: Dict containing the Lambda function event data
        context: Lambda runtime context
    Returns:
        Dict containing status message
    """

    http_method = event["requestContext"]["http"]["method"]

    try:
        if http_method == "GET":

            recipe_id = get_path_param(event, "id")
            if recipe_id:
                # RouteKey: 'GET /recipes/{id}'
                recipe = Recipe.get_recipe(recipe_id)
                return {
                    "statusCode": 200,
                    "body": json.dumps(recipe.to_dict()),
                }
            # RouteKey: 'GET /recipes'
            response = Recipe.get_all_recipes()
            return {
                "statusCode": 200,
                "body": json.dumps(response, indent=2),
            }

        if http_method == "PUT":
            id = get_path_param(event, "id")
            list_name = get_path_param(event, "list_name")
            if id and list_name:
                # RouteKey: 'PUT /recipes/{id}/{list_name}'
                # body should be similar to { "ingredients": "new ingredient" }
                new_list_item = json.loads(event["body"])
                if len(new_list_item.keys()) != 1:
                    raise ServiceError(
                        "Invalid request body",
                        400,
                        {"error": "Invalid request body"},
                    )
                key = list(new_list_item.keys())[0]
                recipe = Recipe.get_recipe(id)
                if key in ["ingredients", "instructions", "tags"]:
                    return {
                        "statusCode": 200,
                        "body": json.dumps(recipe.add_list_item(list_name, new_list_item[key])),
                    }
            if not id and not list_name:
                # RouteKey: 'PUT /recipes'
                new_recipe = json.loads(event["body"])
                if "id" in new_recipe:
                    raise ServiceError(
                        "Cannot add recipe with 'id' field set",
                        400,
                        {"error": "Cannot add recipe with 'id' field set"},
                    )
                recipe = Recipe(new_recipe)
                return {
                    "statusCode": 200,
                    "body": json.dumps(recipe.add_recipe()),
                }
            raise ServiceError(
                "Invalid path parameters",
                400,
                {"error": "Invalid path parameters"},
            )

        if http_method == "POST":
            id = get_path_param(event, "id")
            list_name = get_path_param(event, "list_name")
            index = get_path_param(event, "index")
            body = json.loads(event["body"])
            if id and list_name and index is not None:
                # RouteKey: 'POST /recipes/{id}/{list_name}/{index}'
                body = json.loads(event["body"])
                if list_name in ["ingredients", "instructions", "tags"]:
                    new_value = None
                    try:
                        new_value = body[list_name]
                    except KeyError:
                        raise ServiceError(
                            f"Missing '{list_name}' field in request body",
                            400,
                            {"error": f"Missing '{list_name}' field in request body"},
                        )
                    recipe = Recipe.get_recipe(id)
                    try:
                        current_value = recipe.to_dict()[list_name][int(index)]
                    except IndexError:
                        raise ServiceError(
                            f"Index '{index}' out of range",
                            400,
                            {"error": f"Index '{index}' out of range"},
                        )
                    return {
                        "statusCode": 200,
                        "body": json.dumps(
                            recipe.update_list_item(list_name, int(index), new_value)
                        ),
                    }
            if id and not list_name and not index:
                # RouteKey: 'POST /recipes/{id}'
                recipe = Recipe.get_recipe(id)
                body = json.loads(event["body"])
                for key, value in body.items():
                    if key in ["ingredients", "instructions", "tags", "id"]:
                        raise ServiceError(
                            f"Cannot update '{key}' field",
                            400,
                            {"error": f"Cannot update '{key}' field"},
                        )
                    elif key not in [
                        "title",
                        "description",
                        "image",
                        "source",
                        "original_url",
                        "makes",
                        "active",
                        "notes",
                        "our_notes",
                    ]:
                        raise ServiceError(
                            f"Cannot update '{key}' field",
                            400,
                            {"error": f"Cannot update '{key}' field"},
                        )
                recipe = Recipe.get_recipe(id)
                return {
                    "statusCode": 200,
                    "body": json.dumps(recipe.update_recipe(body)),
                }
            raise ServiceError(
                "Invalid path parameters",
                400,
                {"error": "Invalid path parameters"},
            )

        if http_method == "DELETE":
            id = get_path_param(event, "id")
            list_name = get_path_param(event, "list_name")
            index = get_path_param(event, "index")
            if id and list_name and index is not None:
                # RouteKey: 'DELETE /recipes/{id}/{list_name}/{index}'
                recipe = Recipe.get_recipe(id)
                try:
                    current_value = recipe.to_dict()[list_name][int(index)]
                except IndexError:
                    raise ServiceError(
                        f"Index '{index}' out of range",
                        400,
                        {"error": f"Index '{index}' out of range"},
                    )
                return {
                    "statusCode": 200,
                    "body": json.dumps(recipe.delete_list_item(list_name, int(index))),
                }
            if id and not list_name and not index:
                # RouteKey: 'DELETE /recipes/{id}'
                recipe = Recipe.get_recipe(id)
                recipe.delete_recipe()
                return {
                    "statusCode": 200,
                    "body": "{}",
                }
            raise ServiceError(
                "Invalid path parameters",
                400,
                {"error": "Invalid path parameters"},
            )

        raise ServiceError(
            "Invalid HTTP method",
            400,
            {"error": "Invalid HTTP method"},
        )
    except ServiceError as e:
        return json.dumps(e.client_return())
    except Exception as e:
        print(e)
        return json.dumps({"statusCode": 500, "error": str(e)})
