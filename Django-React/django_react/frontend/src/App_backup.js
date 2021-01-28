import './App.css';
import React, { Component, useState } from 'react';
// bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button,
        Card, CardBody, CardTitle, CardText, Collapse
} from 'reactstrap';
// link
import {Link, Route, Switch, BrowserRouter as Router} from 'react-router-dom';
import Todo from './Todo';
import Home from './Home';
import Gugudan from './Gugudan';

class App extends Component  {
    constructor(props){
        super(props);
        this.state = {
            posts: [],
            isOpen: []
        };
        this.toggle = this.toggle.bind(this);
    }
    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/');
            const posts = await res.json();
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }
    toggle(){
        this.setState(state => ({
            isOpen: !state.isOpen
        }))
    }

    render() {


        return (
            <div class='container'>
                <Router>
                    <header>
                        {this.state.posts.map(item => (
                            <div key={item.id} >
                                <Link to={item.name}>
                                    <Button color='success' onClick={this.toggle}><h3>{item.name}</h3></Button>
                                </Link>
                                    <Collapse isOpen={this.state.isOpen}>
                                        <CardBody>{item.about}</CardBody>
                                    </Collapse>

                            </div>
                        ))}
                    </header>
                    <main>
                        <Card>
                            <CardBody>
                                <Switch>
                                <Route exact path='/Home' component={Home}/>
                                <Route path='/Todo' component={Todo}/>
                                <Route path='/Gugudan' component={Gugudan}/>
                                </Switch>
                            </CardBody>
                        </Card>
                    </main>
                </Router>
            </div>
        );
    }
}
export default App;
