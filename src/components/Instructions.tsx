import './Instructions.css';
import ListGroup from 'react-bootstrap/ListGroup';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


function Instructions() {
    return (
        <section>
            <Container>
                <Row>
                    <Col>
                        <label>Instructions</label>
                        <ListGroup>
                            <ListGroup.Item></ListGroup.Item>
                            <ListGroup.Item>Preheat oven to 375 degrees. Lightly grease a muffin tin (I use olive oil).</ListGroup.Item>
                            <ListGroup.Item>Cook the quinoa. Bring 3/4 up water to a boil, pour in 1/2 cup dry quinoa, reduce to a simmer until fluffy-about 12 minutes.</ListGroup.Item>
                            <ListGroup.Item>Mix applesauce, mashed banana, almond milk, honey and vanilla in a bowl.</ListGroup.Item>
                            <ListGroup.Item>Mix dry ingredients (quinoa, oats, cinnamon) in a separate bowl. Slowly stir the wet into the dry until fully combined.</ListGroup.Item>
                            <ListGroup.Item>Peel core and chop up an apple. Mix the apple chunks into the bowl.</ListGroup.Item>
                            <ListGroup.Item>Fill each of the muffin cups to the top with the quinoa mixture. Add a banana slice or two to the top of each.</ListGroup.Item>
                            <ListGroup.Item>Bake for 20-25 minutes.</ListGroup.Item>
                            <ListGroup.Item>Let cool for 5 minutes, then enjoy one warm!</ListGroup.Item>
                        </ListGroup>
                    </Col>
                </Row>
            </Container>
        </section>
    );
}

export default Instructions;