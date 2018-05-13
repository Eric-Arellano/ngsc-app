import React from 'react'
import Button from '../Button'

describe('<Button />', () => {

  it('performs callback when clicked', () => {
    let callbackTriggered = false
    const wrapper = shallow(<Button handleClick={() => callbackTriggered = true} />)
    expect(callbackTriggered).toBe(false)
    wrapper.find('button').simulate('click')
    expect(callbackTriggered).toBe(true)
  })

})