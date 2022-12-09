import React from 'react'
import styled from 'styled-components'
import { Card } from 'antd';

const { Meta } = Card;

const ItemContainerDiv = styled.a`
	width: 160px;
	text-decoration: none;
	color: black;
	:hover {
		color:black; 
    text-decoration:none; 
    cursor:pointer;
	}
`

const ArtistItem = (props) => {

  return (
		<ItemContainerDiv href={props.item.url} target="_blank">
			<Card
				hoverable
				style={{ width: 160 }}
				cover={<img src={props.item.image} />}
			>
				<Meta title={props.number + ". " +props.item.name} style={{ textAlign: 'center' }}/>
			</Card>
    </ItemContainerDiv>
  )
}

export default ArtistItem