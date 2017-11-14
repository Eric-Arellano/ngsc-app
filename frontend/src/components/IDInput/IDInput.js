// @flow
import React from 'react'
import { Form, FormGroup, FormControl, ControlLabel, HelpBlock, Button, Tooltip } from 'react-bootstrap'

type Props = {
  handleKeyInput: (e: SyntheticInputEvent<HTMLInputElement>) => void,
  handleEnterKey: (e: SyntheticInputEvent<HTMLInputElement>) => void,
  handleSubmit: () => void,
  currentValue: string,
  validationState: ?string,
  submissionFailed: boolean
}

const IDInput = (props: Props) => {
  const {handleKeyInput, handleEnterKey, handleSubmit, currentValue, validationState, submissionFailed} = props
  return (
    <Form inline>
      <FormGroup controlId={'ID'} validationState={validationState}>
        <ControlLabel>Student ID:</ControlLabel>
        {' '}
        <FormControl type={'text'} value={currentValue} onKeyDown={handleEnterKey} onChange={handleKeyInput}  />
        <FormControl.Feedback/>
        <HelpBlock>Please enter a valid student ID.</HelpBlock>
      </FormGroup>
      <Button onClick={handleSubmit}>Submit</Button>
      {submissionFailed &&
      <Tooltip placement={'right'} className={'in'} id={'tooltip-right'}>Fix your ID before submitting!</Tooltip>}
    </Form>
  )
}

export default IDInput