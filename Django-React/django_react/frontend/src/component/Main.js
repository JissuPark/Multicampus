import React, {Component} from 'react';

import Header from './Header';
import Body from './Body';


class Main extends Component{
    constructor(props){
        super(props);
        this.state={
        };
    }

    render(){
        return (
            <div className='Main'>
                <Header/>
                <Body />
            </div>
        );
    }


}

export default Main;