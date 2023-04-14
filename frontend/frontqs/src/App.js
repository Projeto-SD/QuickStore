import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import TelaInicial from './telas/TelaInicial.js';
import TelaProduto from './telas/TelaProduto.js';
import { Link } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div>
        <header><div className='Teste'><Link to="/">QuickStore</Link></div></header>
        <main>
          <Routes>
            <Route path="/" element={<TelaInicial />} />
            <Route path="/produto/:nome" element={<TelaProduto />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
