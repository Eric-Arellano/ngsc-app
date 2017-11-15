// @flow
import React from 'react'
import { Form, FormGroup, FormControl, ControlLabel, HelpBlock, Button } from 'react-bootstrap'



const IDInput = (props: Props) => {

  type Props = {
    handleKeyInput: (e: SyntheticInputEvent<HTMLInputElement>) => void,
    handleEnterKey: (e: SyntheticInputEvent<HTMLInputElement>) => void,
    handleSubmit: () => void,
    currentValue: string,
    validationState: ?string,
    submitDisabled: boolean
  }

  const {handleKeyInput, handleEnterKey, handleSubmit, currentValue, validationState, submitDisabled} = props

  return (
    <Form inline>
      <FormGroup controlId={'ID'} validationState={validationState}>
        <ControlLabel>Student ID:</ControlLabel>
        {' '}
        <FormControl type={'text'} value={currentValue} placeholder="Enter Student ID" onKeyDown={handleEnterKey} onChange={handleKeyInput}  />
        <FormControl.Feedback/>
        <HelpBlock>Please enter a valid student ID.</HelpBlock>
      </FormGroup>
    <br/>
    <Button className="ngsc" disabled={submitDisabled} onClick={handleSubmit}>Submit</Button>
    </Form>
  )
}

export default IDInput