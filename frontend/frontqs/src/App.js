import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import TelaInicial from './telas/TelaInicial.js';
import TelaProduto from './telas/TelaProduto.js';
import { Link } from "react-router-dom";
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import { LinkContainer } from 'react-router-bootstrap'

function App() {
  return (
    <BrowserRouter>
      <div className='d-flex flex-column site-container'>
        <header>
          <Navbar bg="dark" variant="dark">
            <Container>
              <LinkContainer to="/">
                <Navbar.Brand>QuickStore</Navbar.Brand>
              </LinkContainer>
            </Container>
          </Navbar>
        </header>
        <main>
          <Container>
            <Routes>
              <Route path="/" element={<TelaInicial />} />
              <Route path="/produto/:nome" element={<TelaProduto />} />
            </Routes>
          </Container>
        </main>
        <footer>
          <div className='text-center'>QuickStore ® </div>
        </footer>
      </div>
    </BrowserRouter>
  );
}

export default App;
