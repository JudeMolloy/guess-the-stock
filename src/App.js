import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";

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
        ... no changes in this part ...
        <p>The current time is {placeholder}</p>
      </header>
    </div>
  );
}

export default App;
