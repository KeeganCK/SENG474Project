import React, { useState } from 'react';
import { AutoComplete } from 'antd';


const Genre = () => {
  const [value, setValue] = useState('');
  const [options, setOptions] = useState([]);

	const genres = ['pop', 'rock', 'country', 'dance']
  const getGenres = (text) => {
		const re = new RegExp(text);
		const genresObjectArray = []
		genres.forEach(genre => {
			if(genre.match(re)) {
				const genresObject = {};
				genresObject.value = genre
				genresObjectArray.push(genresObject);
			}
		})
		console.log(genresObjectArray)
		return genresObjectArray;
	}

  const onSearch = (searchText) => {
    setOptions(
      searchText ? getGenres(searchText) : []
    );
  };
  const onSelect = (data) => {
    console.log('data: ', data);
  };
  const onChange = (data) => {
    setValue(data);
  };
  return (
    <>
      <AutoComplete
        value={value}
        options={options}
        style={{
          width: 500,
        }}
        onSelect={onSelect}
        onSearch={onSearch}
        onChange={onChange}
        placeholder="Genre"
      />
    </>
  );
};
export default Genre;