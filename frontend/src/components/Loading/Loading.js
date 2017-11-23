import React from 'react'
import './Loading.css'

const Loading = () => (
  <section className={'loadingContainer'}>
    <div className={'loadingSvgContainer'}>
      <svg className={'loadingSvg'} viewBox={'25 25 50 50'}>
        <circle className={'loadingPath'} cx={50} cy={50} r={20} fill={'none'} strokeWidth={1} strokeMiterlimit={10} />
      </svg>
    </div>
  </section>
)

export default Loading