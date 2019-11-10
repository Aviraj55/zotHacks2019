import React from 'react';
import { Route, Switch, Router } from 'react-router-dom';
import history from './history';
import 'bootstrap/dist/css/bootstrap.min.css';

import {
    UserInput,
} from './view';

function App() {
    console.log('Print')
    return (
        <div>
            <Router history={history}>
                <Switch>
                    <Route exact path='/' component={UserInput}/>
                </Switch>
            </Router>
        </div>
    );
}

export default App;