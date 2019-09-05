import React from 'react';
import logo from './logo.svg';
import axios from "axios";
import './App.css';

// https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react

class App extends React.Component {
    constructor(){
        super();
        this.state = {
            data : [],
            names: []
        }
    }

    componentDidMount() {
        this.getPlayersData();
    }

    getPlayersData = () => {
        axios
            .get("http://localhost:8000/api/players/")
            .then(response => {
                this.setState({data: response.data});
                console.log(response)
            })
            .catch(err => console.log(err))
    };

    getPlayersNames = () => {
        return this.state.data.map(
            playerData => <li>playerData.name</li>
        )
    };


    render() {
        const data = this.state.data;
        const playerNames = data.map((playerData) =>
            <li key={playerData.name}>{playerData.name}</li>
        );

        return (
            <div>
                Players:
                {playerNames}
            </div>
        );
    }
}

export default App;
