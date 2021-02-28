import React, { useState, useEffect } from "react";
import { InputText } from "primereact/inputtext";
import Leaderboard from "./components/leaderboard";
import { Button } from "primereact/button";

import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";

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
        <div className="p-formgroup-inline p-jc-center">
          <div className="p-field">
            <InputText id="name" type="text" placeholder="Name" />
          </div>
          <Button type="button" label="Start" />
        </div>
        <div className="p-m-6">
          <h2>Leaderboard</h2>
          <Leaderboard />
        </div>
      </main>
      <footer>Jude & Michael</footer>
    </div>
  );
}

export default App;
