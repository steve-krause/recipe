import './App.css'
import ListGroup from 'react-bootstrap/ListGroup';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Image from 'react-bootstrap/Image';

function App() {

  return (
    <>
      <title>Apple Banana Quinoa Breakfast Cups</title>
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand href="#home">Recipes</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
            <Nav>
              <NavDropdown title="Browse">
                <NavDropdown.Item href="#categories">Category</NavDropdown.Item>
                <NavDropdown.Item href="#tags">Tags</NavDropdown.Item>
                <NavDropdown.Item href="#ingredients">
                  Ingredients
                </NavDropdown.Item>
              </NavDropdown>
              <Nav.Link href="#search">Search</Nav.Link>
              <Nav.Link href="#logout">Logout</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
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
    </>
  );
}

export default App
