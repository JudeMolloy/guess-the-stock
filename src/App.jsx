import React, { useState, useEffect } from "react";
import { InputText } from "primereact/inputtext";
import Leaderboard from "./components/leaderboard";
import { Button } from "primereact/button";

import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";
import PrimeReact from "primereact/api";

function App() {
  const [placeholder, setPlaceholder] = useState("Hi");

  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setPlaceholder(data.result);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Guess the stock</h1>
      </header>
      <main>
        <div className="p-d-flex p-jc-center">
          <span className="p-float-label">
            <InputText id="in" />
            <label htmlFor="in">Username</label>
          </span>
          <Button label="Start" />
        </div>

        <h2>Leaderboard</h2>
        <Leaderboard />
      </main>
      <footer>Jude & Michael</footer>
    </div>
  );
}

export default App;
