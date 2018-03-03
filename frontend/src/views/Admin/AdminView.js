// @flow
import React from 'react'
import { Button, Input, Label, RadioGroup } from 'components'

const updateCurrentSelection = (s: string) => {

}

const actionList = [
  'Create empty file',
  'Create empty folder',
  'Copy file',
  'Copy folder',
  'Move file',
  'Move folder',
  'Remove file',
  'Remove folder',
  'Rename file',
  'Rename folder',
]

const fileType = [
  'Google doc',
  'Google sheet',
  'Google slide',
  'Google form',
]

const AdminView = () => (
  <div>
    <section>
      <p>This will be the admin view.</p>
    </section>
    <br />

    <section>
      <p>Choose which groups you would like to apply the action to:</p>
      <ul>
        <li>Committee chair folders</li>
        <li>Committee lead folders</li>
        <li>Mission team folders</li>
        <li>Section leader folders</li>
      </ul>
    </section>
    <br />

    <section>
      <p>Choose which action you'd like to take:</p>
      <RadioGroup options={actionList} updateCurrentSelection={updateCurrentSelection} />
    </section>
    <br />

    <section>
      <p>Supply the necessary information:</p>
      <Label>Source file name:</Label>
      <Input placeholder='ex: Leadership/Retreat 1/Google Drive.gslides' />
    </section>
    <br />

    <section>
      <p>[IF ACTION HAS FILE] Choose which file type?</p>
      <RadioGroup options={fileType} updateCurrentSelection={updateCurrentSelection} />
    </section>
    <br />

    <section>
      <Button>Submit</Button>
    </section>

  </div>
)

export default AdminView