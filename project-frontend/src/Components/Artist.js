import React, { useState } from 'react';
import { Input, Radio, Typography, notification } from 'antd';
import styled from 'styled-components';

const { Title, Text } = Typography;

const { Search } = Input;

const InputContainerDiv = styled.div`
  width: 50%;
  margin: auto;
  margin-top: 2em;
  display: flex;
  flex-direction: column;
  align-items: center;
`

const RadioContainerDiv = styled.div`
  margin-bottom: 1em;
  display: flex;
  flex-direction: row;
  align-items: end;
`


const Artist = (props) => {
  const [loading, setLoading] = useState(false);
  const [type, setType] = useState('CosCV')

  const options = [
    {
      label: 'CosCV',
      value: 'CosCV',
    },
    {
      label: 'CosTF',
      value: 'CosTF',
    },
    {
      label: 'EudCV',
      value: 'EudCV',
    },
    {
      label: 'EudTF',
      value: 'EudTF',
    },
  ];

  const onChange1 = ({ target: { value } }) => {
    console.log('radio1 checked', value);
    setType(value);
  };

  const onGetArtist = async (value) => {
    console.log(value)
    try {
      setLoading(true);
      const response = await fetch(`http://127.0.0.1:5000/getArtist`, {
				method: 'POST',
        headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
          name: value,
          type: type
        })
			})
			const responseData = await response.json();
			console.log(responseData);
			if(!response.ok) {
				throw new Error(responseData.message);
			}
      props.setTopTen(responseData.data);
      props.setTopTenSpot(responseData.spotifyData);
      setLoading(false);
    } catch (err) {
      console.log(err);
      notification.error({
        message: 'An error occured',
        description: 'Most likely a wrongly spelt name or expired API key'
      })
      setLoading(false);
    }
  }
  
  return (
    <>
    <InputContainerDiv>
      <RadioContainerDiv>
        <Title level={5} style={{ marginRight: '8px' }}>Algorithms: </Title>
        <Radio.Group options={options} onChange={onChange1} value={type} optionType="button"/>
      </RadioContainerDiv>
      <Search placeholder="Enter Artist Name" enterButton="Get Artist" loading={loading} onSearch={onGetArtist}/>
    </InputContainerDiv>
    </>
  );
};
export default Artist;