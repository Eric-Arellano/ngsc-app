// @flow
import React, { Component } from 'react'
import { Header } from 'components'
import { StudentInfoContainer, RequirementsContainer } from 'containers';
import { getUserInfo } from 'utils/api'

type Props = { }

type State = {
  isValidated: boolean,
  id?: number,
  firstName: string,
  lastName: string,
}

const Test = ({ }) => (
  <h1>{'test'}</h1>
)

// const x = () => { console.log('x') }
// this.setState({
//   isLoading: true
// }, () => {
//   console.log(this.state.isLoading)
// })
// console.log(this.state.isLoading)


// components/Dashboard
// components/Dashboard.js
// components/Dashboard.scss

// containers/Dashboard/DashboardContainer.js

// DashboardContainer -->
// render() {
//   return (
//     <Dashboard {...this.state}
//   )
// }
// const Dashboard = ({ id, firstName }) => (

// )


class AppContainer extends Component<Props, State> {

  // real code
  // state = {
  //   id: 0,
  //   firstName: '',
  //   lastName: '',
  // };

  // demo
  state = {
    isLoading: false,
    isValidated: false,
    isVerified: false,
    id: null,
    name: {
      first: '',
      last: ''
    },
    isPopupOpen: false

  };

  // updateValidatedUser = (value: boolean) => {
  //   this.setState({
  //     isValidated: value
  //   })
  // };

  // updateID = (value: number) => {
  //   this.setState({
  //     id: value
  //   })
  // };

  // updateName = (firstName: string, lastName: string) => {
  //   this.setState({
  //     firstName: firstName,
  //     lastName: lastName
  //   })
  // };
  verifyStudentId = (id) => {
    getUserInfo(id)
      .then(data => {
        console.log('then')
        this.setState({
          isLoading: false,
          isValidated: true,
          name: {
            first: data.firstName,
            last: data.lastName
          },
          id
        })
      })
      .catch(err => {
        console.log('catch')
        const mockData = {
          name: {
            first: 'eric',
            last: 'arellano'
          },
          id
        }
        console.log(err)
        this.setState({
          isLoading: false,
          isValidated: false,
          name: mockData.name,
          id: mockData.id
        }, this.confirmCorrectStudent)
      })
  }

  confirmCorrectStudent = (isConfirmed) => {
    this.setState({ isPopupOpen: true }, () => {
      /* eslint-disable */
      const answer = confirm('is this you?')
      /* eslint-enable */
      console.log(answer)
      this.setState({ isVerified: isConfirmed, isPopupOpen: false })
    })
  }


  render() {
    const { isValidated, isVerified, id, name, isPopupOpen } = this.state
    return (
      <div className="App">
        <Header />
        { isValidated && isVerified
          ? <RequirementsContainer id={id} name={name} />
          : <StudentInfoContainer verifyStudentId={this.verifyStudentId} confirmCorrectStudent={this.confirmCorrectStudent} />
        }
        { isPopupOpen && <Test /> }
      </div>
    );
  }
}

export default AppContainer;
