import './Information.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Image from 'react-bootstrap/Image';


function Information() {
    return (
        <section>
            <Container>
                <Row>
                    <Col>
                        <label>Title</label>
                        <p>Apple Banana Quinoa Breakfast Cups</p>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <label>Description</label>
                        <p>This lksjdfl;ajs kjlsadjf fjsdfj fasdjlkfjlks fjsd jjflkdsjj jdslkfjsdlk  jfkdsljflks jfks  jskdflj jas dfj.</p>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Image src='/banana-quinoa-muffins-vegan-1.webp' fluid className='image' />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <label>Notes</label>
                        <p>This is a pain in the ass to make</p>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <label>Original Source</label>
                        <p><a href='http://www.skinnytaste.com/2011/09/baked-eggplant-sticks.html'>http://www.skinnytaste.com</a></p>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <label>Yield</label>
                        <p></p>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <label>Active</label>
                        <p></p>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <label>Total</label>
                        <p></p>
                    </Col>
                </Row>
            </Container>
        </section>
    );
}

export default Information;