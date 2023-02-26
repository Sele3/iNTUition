export function UploadBar(props) {

  return (
    <div style={{ position: 'absolute', top: '15%', left: "2%", width: "25%"}}>
      <div class="flex justify-center">

<div class="flex flex-col items-center my-20 bg-[#f7f7f7] sm:w-3/4 sm:rounded-lg sm:shadow-xl">
    <div class="mt-10 mb-10 text-center">
        <h2 class="text-2xl font-semibold mb-2">Upload your files</h2>
        <p class="text-xs text-gray-500">File should be of format .pdf</p>
    </div>
    <form action="#" class="relative w-4/5 h-32 max-w-xs mb-10 bg-[#ececec] hover:bg-gray-200 rounded-lg shadow-inner">
        <input type="file" id="file-upload" class="hidden" onChange={props.handleFileChange}/>
        <label for="file-upload" class="z-20 flex flex-col-reverse items-center justify-center w-full h-full cursor-pointer">
        {props.selectedFile ? <p class="z-10 text-xs font-light text-center text-gray-500">{props.selectedFile.name}</p> : <p class="z-10 text-xs font-light text-center text-gray-500">Attach a file</p>}
            <svg class="z-10 w-8 h-8 text-indigo-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
            </svg>
        </label>
    </form>
    <button onClick = {props.onClick} className="bg-blue-500 font-light hover:bg-blue-700 text-white py-2 px-4 rounded-full -translate-y-5">
  Upload
</button>
</div>
</div>
    </div>
  );
}
