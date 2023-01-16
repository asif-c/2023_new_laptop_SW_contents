import logo from './logo.svg';
import './App.css';
import axios from "axios";
import React, { useState } from 'react';

function App() {
  //return (
  //  <div className="App">
  //    <header className="App-header">
  //      <img src={logo} className="App-logo" alt="logo" />
  //      <p>
  //        Edit <code>src/App.js</code> and save to reload.
  //      </p>
  //      <a
  //        className="App-link"
  //        href="https://reactjs.org"
  //        target="_blank"
  //        rel="noopener noreferrer"
  //      >
  //        Learn React
  //      </a>
  //    </header>
  //  </div>
  //);

    const [mess, setMess] = useState(null)

    function getData() {
        axios.get("http://127.0.0.1:5000")
             .then(response => {setMess(response.data) })
    }

    return (
        <>
            <button onClick={getData}>Find SensEh version</button>
            <p>{mess}</p>

        </>
        );

}

export default App;
