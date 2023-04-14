import TelaInicial from "./TelaInicial";
import App from "../App";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom"

function TelaProduto() {
    const params = useParams();
    const { nome } = params;
    return (
        <div>
            <h1> {nome} </h1>
        </div>

    );
}
export default TelaProduto;