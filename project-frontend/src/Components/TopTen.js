import React, { useState } from 'react'
import styled from 'styled-components'
import Artist from './Artist'
import { Table, Typography } from 'antd';

const { Title, Text } = Typography;


const MainContainerDiv = styled.div`
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	margin-top: 2em;
`

const TableDiv = styled.div`
	margin-right: 50px;
`

const columns = [
	{
    title: 'Ranking',
		key: 'position',
    render: (_, record) => (
      <Text>{record.position}</Text>
    ),
		align: 'center'
  },
	{
    title: 'Image',
    dataIndex: 'iamge',
    key: 'image',
		render: (_, record) => (
      <img style={{ height: '48px', width: '48px' }} src={record.image} />
    ),
  },
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
		render: (_, record) => (
      <a href={record.url} target="_blank">{record.name}</a>
    ),
  },
	{
    title: 'Score',
    dataIndex: 'score',
    key: 'score',
  },
]

const columnsSpot = [
	{
    title: 'Ranking',
		key: 'position',
    render: (_, record) => (
      <Text>{record.position}</Text>
    ),
		align: 'center'
  },
	{
    title: 'Image',
    dataIndex: 'iamge',
    key: 'image',
		render: (_, record) => (
      <img style={{ height: '48px', width: '48px' }} src={record.image} />
    ),
  },
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
		render: (_, record) => (
      <a href={record.url} target="_blank">{record.name}</a>
    ),
  },
]

const TopTen = () => {
  const [topTen, setTopTen] = useState([])
  const [topTenSpot, setTopTenSpot] = useState([])

  return (
    <div>
			<Artist setTopTen={setTopTen} setTopTenSpot={setTopTenSpot}/>
			<MainContainerDiv>
				{topTen.length > 0 && 
					<TableDiv>
						<Title level={4} style={{ textAlign: 'center' }}>Our Reccomendations</Title>
						<Table columns={columns} dataSource={topTen} pagination={false} bordered={true}/>
					</TableDiv>
				}
				{topTenSpot.length > 0 &&
					<TableDiv>
						<Title level={4} style={{ textAlign: 'center' }}>Spotify Reccomendations</Title>
						<Table columns={columnsSpot} dataSource={topTenSpot} pagination={false} bordered={true}/>
					</TableDiv>
				}
			</MainContainerDiv>
		</div>
  )
}

export default TopTen