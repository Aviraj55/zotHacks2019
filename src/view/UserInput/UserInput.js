//profile id, Auth token
import React, { useState } from "react";
import './UserInput.scss';
import axios from 'axios';

import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { strict } from "assert";

function UserInput(props){

    const [UserInput, setUserArr] = useState([])
    const [theUser, setUser] = useState({
        'Id': ''
    });

    function handleInput(x) {
        setUser({
            'Id': x.target.value
        });
        console.log(x.target.name)
    }

    function handleSubmit(x) {
        x.preventDefault()
        console.log(theUser)
        setUserArr([...UserInput, theUser]);
        // axios.post('/UserInput', theUser).then(res => {
        //    console.log(res.data);
        // }).catch(err => {
        //     console.log("Does not work");
        // })
        fetch('http://localhost:5000/?Id=' + theUser['Id'])
    }

    return (
        <div>
            <p></p>
            <Form.Label>Spotify Id</Form.Label>
            <Form.Control Id = "Id" onChange={handleInput}></Form.Control>
            <Button onClick={handleSubmit}>Submit</Button>
        </div>
    )
}

export default UserInput;