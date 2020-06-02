import React, { Component } from "react";
import ReactDOM from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/anestesias")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <div className="container">
        <h3>Listado de Hojas de Anestesia</h3>
        <br />
        <ul>
          {this.state.data.map((anestesia) => {
            return (
              <li key={anestesia.id}>
                {anestesia.paciente} - {anestesia.dia_cirugia} -{" "}
                {anestesia.tipo_cirugia} - {anestesia.cirujano}
              </li>
            );
          })}
        </ul>
      </div>
    );
  }
}

export default App;

ReactDOM.render(<App />, document.getElementById("app"));
