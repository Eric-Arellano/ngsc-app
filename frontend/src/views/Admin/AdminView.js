// @flow
import React from 'react'
import { Button, Input, Label } from 'components'

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
      <ul>
        <li>Create empty file</li>
        <li>Create empty folder</li>
        <li>Copy file</li>
        <li>Copy folder</li>
        <li>Move file</li>
        <li>Move folder</li>
        <li>Remove file</li>
        <li>Remove folder</li>
        <li>Rename file</li>
        <li>Rename folder</li>
      </ul>
    </section>
    <br />

    <section>
      <p>Supply the necessary information:</p>
      <Label>Source file name:</Label>
      <Input placeholder='ex: Leadership/Retreat 1/Google Drive.gslides' />
      <p>[IF ACTION HAS FILE] Choose which file type?</p>
      <ul>
        <li>Google Form</li>
        <li>Google Doc</li>
        <li>Google Sheet</li>
        <li>Google Slides</li>
      </ul>
    </section>
    <br />

    <section>
      <Button>Submit</Button>
    </section>
  </div>
)

export default AdminView