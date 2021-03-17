import React, { Component } from 'react';
import axios from 'axios';

class Gugudan extends Component {
    constructor(props){
        super(props);
        this.state = {
            dans: [],
            selected: 0
        };
        this.display = this.display.bind(this);
    }


    getpost = async() => {
        const {data}= await axios.get('/Gugudan/');
        this.setState({dans:{data}.data});
    }

    async componentDidMount() {
       this.getpost();
    }

    //component 출력 함수
    display = () => {
        const multiplier = this.state.selected;
        const multiplicand = [1,2,3,4,5,6,7,8,9];
        if (multiplier === 0){
            return(
                <pre>{`숫자를 선택하면 선택된 숫자의 구구단을 출력해줍니다.
                원하는 단을 선택해보세요!`}</pre>
            );
        }
        return(
            <table className='table table-hover text-center'>
            <thead>
                <tr>
                    <th colspan='5'>
                        {multiplier}단을 선택하셨습니다.
                    </th>
                </tr>
            </thead>
            <tbody>
            {multiplicand.map((mtc)=>{
                return(
                <tr key={mtc}>
                    <td>{multiplier}</td>
                    <td> x </td>
                    <td>{mtc}</td>
                    <td> = </td>
                    <td>{multiplier*mtc}</td>
                </tr>);
            })}
            </tbody>
            </table>
        );
    }

    //선택된 dan을 받아서 state변수에 저장 후 출력함수 호출
    handleChange =(event)=> {
        event.preventDefault();
        this.setState({selected: event.target.selectedIndex});
        this.display();
    }



    render() {
        return (
            <div className='container'>
                <div className='d-flex justify-content-center'>
                    <h1>구구단 출력</h1> <small className='mt-4'>by JavaScript</small>
                </div>
                <label className='mt-3'>
                    몇 단을 출력하시겠습니까?
                </label>
                <select className='custom-select' onChange={this.handleChange}>
                    <option value='' selected disabled hidden>단을 선택해주세요</option>
                    {this.state.dans.map(item => (
                        <option
                            key={item.id}
                            value={item.dan}
                        >
                        {item.dan}
                        </option>
                    ))}
                </select>

                <hr/>
                {this.display()}

            </div>
        );
    }
}
export default Gugudan;
