import React from "react";
import { Button } from "primereact/button";
import { InputText } from "primereact/inputtext";

class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    alert("A name was submitted: " + this.state["value"]);
    event.preventDefault();
  }

  render() {
    return (
      <div className="p-formgroup-inline p-jc-center">
        <div className="p-field">
          <InputText
            id="name"
            type="text"
            placeholder="Name"
            value={this.state.value}
            onChange={this.handleChange}
          />
        </div>
        <Button type="button" label="Start" onClick={this.handleSubmit} />
      </div>
    );
  }
}

export default NameForm;
