import React, { useState } from 'react';
import { Input } from 'antd';
import styled from 'styled-components';

const { Search } = Input;

const InputContainerDiv = styled.div`
  width: 50%;
  margin: auto;
  margin-top: 2em;
`


const Artist = (props) => {
  const [loading, setLoading] = useState(false);

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
          name: value
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
      setLoading(false);
    }
  }
  
  return (
    <>
    <InputContainerDiv>
      <Search placeholder="Enter Artist Name" enterButton="Get Artist" loading={loading} onSearch={onGetArtist}/>
    </InputContainerDiv>
    </>
  );
};
export default Artist;