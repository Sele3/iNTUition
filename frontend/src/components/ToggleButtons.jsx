
export function ToggleButtons(props){
    return (
        <div className="flex space-x-2">
          <button style = {{height : "5%"}}
            className={`bg-blue-500 text-white font-bold py-2 px-4 rounded ${
              props.mode === "summary" ? "bg-blue-700" : ""
            }`}
            onClick={props.onSum}
          >
            Summary
          </button>
          <button style = {{height : "5%"}}
            className={`bg-gray-400 text-black font-bold py-2 px-4 rounded ${
              props.mode === "ppt" ? "bg-gray-700" : ""
            }`}
            onClick={props.onPpt}
          >
            PowerPoint
          </button>
          <button style = {{height : "5%"}}
            className={`bg-yellow-500 text-black font-bold py-2 px-4 rounded ${
              props.mode === "info" ? "bg-yellow-700" : ""
            }`}
            onClick={props.onInfo}
          >
            Infographic
          </button>
        </div>
      );
}