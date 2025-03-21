import './Ingredients.css';
import ListGroup from 'react-bootstrap/ListGroup';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


function Ingredients() {
    return (
        <section>
            <Container>
                <Row>
                    <Col>
                        <label>Ingredients</label>
                        <ListGroup>
                            <ListGroup.Item variant='primary'>1/2 cup applesauce</ListGroup.Item>
                            <ListGroup.Item>1 cup mashed banana (about 3 bananas)</ListGroup.Item>
                            <ListGroup.Item>1 banana for slicing</ListGroup.Item>
                            <ListGroup.Item>1 cup cooked quinoa (about 1/2 cup dry)</ListGroup.Item>
                            <ListGroup.Item>2 1/2 cups old-fashioned oats</ListGroup.Item>
                            <ListGroup.Item>1/2 cup almond milk</ListGroup.Item>
                            <ListGroup.Item>1/4 cup honey</ListGroup.Item>
                            <ListGroup.Item>1 tsp vanilla extract</ListGroup.Item>
                            <ListGroup.Item>1 tsp cinnamon</ListGroup.Item>
                            <ListGroup.Item>1 apple, peeled and chopped</ListGroup.Item>
                        </ListGroup>
                    </Col>
                </Row>
            </Container>
        </section>
    );
}

export default Ingredients;