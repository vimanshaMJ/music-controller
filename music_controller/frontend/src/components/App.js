import React, { Component } from "React";
import render from "react-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>Testing react code</h1>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
