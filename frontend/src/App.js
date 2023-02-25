import {UploadBar} from './components/UploadBar';
import {Language} from './components/Language';
import React, { useEffect, useRef,useState } from 'react';
import './index.css';
import { SummaryText } from './components/SummaryText';
import { ToggleButtons } from './components/ToggleButtons';
import axios from 'axios';



const languageOptions = [
  { label: 'English', value: 'en' },
  { label: 'Spanish', value: 'es' },
  { label: 'French', value: 'fr' },
  // Add more language options as needed
];

function App() {
  // state variables
  const stateRef = useRef();
  const [summaryText, setSummaryText] = useState("");
  stateRef.current = summaryText;
  const [mode, setMode] = useState("summary");
  const [selectedFile, setSelectedFile] = useState(null);
  const [isUploaded, setUploaded] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState(languageOptions[0]);
  // callback on summary
  useEffect(()=>{
    console.log(summaryText);
  },[summaryText]);

  // upload functions
  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };
  const handleClick = () =>{
    if(selectedFile){
        const data = new FormData();
        data.append('file', selectedFile, selectedFile.name);
        setUploaded(true);
        axios.post('http://127.0.0.1:8000/api/uploadfile/',data)
        .then(res => {
            if (res) {
                setSummaryText(res);
            } else {
                console.error("Invalid response data:", res);
            }
        })
        .catch(err => {
            console.error("Error uploading file:", err);
        });
    }
}
  // language functions
  const handleLanguageChange = (event) =>{
    const selectedValue = event.target.value;
    const selectedOption = languageOptions.find(option => option.value === selectedValue);
    setSelectedLanguage(selectedOption);
  }
  // mode functions
  const setSumMode = () =>{
    setMode("summary");
  }
  const setPPTMode = () =>{
    setMode("ppt");
  }
  const setInfoMode = () =>{
    setMode("info");
  }
  // render
  return (
    <div className="bg-black flex h-screen justify-center">
      <h1 className="text-white 500 font-thin text-3xl" style = {{position: "absolute", top : "10%"}}>Article Summariser
      </h1>
      {!isUploaded && (
      <Language languageOptions = {languageOptions} handleLanguageChange = {handleLanguageChange} selectedLanguage = {selectedLanguage}></Language>
      )}
      {!isUploaded && (
      <UploadBar selectedFile = {selectedFile} handleFileChange = {handleFileChange} onClick = {handleClick}></UploadBar>
      )}
      {isUploaded && (
      <ToggleButtons mode = {mode} onSum = {setSumMode} onPpt = {setPPTMode} onInfo = {setInfoMode}></ToggleButtons>
      )}
      {summaryText !== "" && isUploaded && (
      <SummaryText summaryText = {summaryText}></SummaryText>
      )}
      
    </div>
  );
}

export default App;
