import '../App.css';
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'

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
        <Row>
            <div className='produtos'>
                {data && data.dados.map(produto => (
                    <Col>
                        <Card key={produto.nome}>
                            <Link to={`/produto/${produto.nome}`}>
                                <img src={produto.imagem_url} className='card-img-top' alt={produto.nome} />
                            </Link>
                            <Card.Body>
                                <Link to={`/produto/${produto.nome}`}>
                                    <Card.Title>
                                        {produto.nome}
                                    </Card.Title>
                                </Link>
                                <Card.Text>
                                    ${produto.preco}
                                </Card.Text>
                                <Button>Adicionar ao pedido</Button>
                            </Card.Body>

                        </Card>
                    </Col>
                ))}
            </div>
        </Row>
    </div>;
}

export default TelaInicial;