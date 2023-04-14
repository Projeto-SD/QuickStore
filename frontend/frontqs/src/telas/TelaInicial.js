import '../App.css';
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function TelaInicial() {

    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get("http://localhost:5000/produt");
            setData(response.data);
        };

        fetchData();
    }, []);

    return <div>
        <h1>Produtos</h1>
        <div className='produtos'>
            {data && data.dados.map(produto => (
                <div className='produto' key={produto.nome}>
                    <Link to={`/produto/${produto.nome}`}>
                        <img src={produto.imagem_url} alt={produto.nome} />
                    </Link>
                    <div className='prod-info'>
                        <Link to={`/produto/${produto.nome}`}>
                            <p>{produto.nome}</p>
                        </Link>
                        <p><strong>${produto.preco}</strong></p>
                        <button>Adicionar ao pedido</button>
                    </div>
                </div>
            ))}
        </div>
    </div>;
}

export default TelaInicial;