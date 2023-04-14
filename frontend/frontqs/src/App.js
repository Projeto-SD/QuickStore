import './App.css';
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get("http://localhost:5000/produt");
      setData(response.data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <header>QuickStore</header>
      <h1>Produtos</h1>
      <div className='Produtos'>
        {data && data.dados.map(produto =>
          <div className='produto' key={produto.slug}>
            <img src={produto.imagem_url} alt={produto.nome} />
            <p>{produto.nome}</p>
            <p>{produto.preco}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
