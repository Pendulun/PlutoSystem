import React from 'react'

export const TagButton = ({ tagId, title, onClick, props }) => (
  <div onClick={onClick}>
    <input type="radio" name="option" id={tagId} class="peer hidden" {...props} />
    <label
      for={tagId}
      class="block cursor-pointer select-none btn-tags peer-checked:bg-gray peer-checked:text-lightBlue peer-checked:border-lightBlue"
      >{title}</label>
  </div>
)