import './Navbar.css'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';


function Header() {

    return (
        <>
            <Navbar expand="lg" className="bg-body-tertiary">
                <Container>
                    <Navbar.Brand href="#home">Recipes</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
                        <Nav>
                            <NavDropdown title="Browse">
                                <NavDropdown.Item href="#categories">Category</NavDropdown.Item>
                                <NavDropdown.Item href="#tags">Tags</NavDropdown.Item>
                                <NavDropdown.Item href="#ingredients">Ingredients</NavDropdown.Item>
                            </NavDropdown>
                            <Nav.Link href="#search">Search</Nav.Link>
                            <Nav.Link href="#logout">Logout</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

export default Header
