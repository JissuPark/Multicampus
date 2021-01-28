import React, {Component} from 'react';
import {Switch, Route} from 'react-router-dom';
//custom
import Home from './app/Home';
import Todo from './app/Todo';
import Gugudan from './app/Gugudan';
import Student from './app/Student';


class Body extends Component{
    constructor(props){
        super(props);
        this.state = {
        };
    }
    render(){
        return(
            <div className='Body'>
                <Switch>
                    <Route exact path={["/","/Home"]} component={Home}/>
                    <Route path="/Todo" component={Todo}/>
                    <Route path="/Gugudan" component={Gugudan}/>
                    <Route path='/Student' component={Student}/>
                </Switch>
            </div>
        );
    }
}
export default Body;