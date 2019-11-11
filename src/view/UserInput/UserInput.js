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
        <div className='Admin'>
            <p className='Topleft'>Zotify</p>
            <div>
                <Form.Label>Make Your Spotify Top Hits</Form.Label>
                <div>
                    <Form.Control placeholder='Enter Spotify User Id' Id = "Id" onChange={handleInput}></Form.Control>
                    <div>
                        <Form.Text></Form.Text>
                        <Button onClick={handleSubmit}>Create Your Playlist</Button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default UserInput;