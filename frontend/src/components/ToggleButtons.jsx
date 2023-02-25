
export function ToggleButtons(props){
    return (
        <div className="">
          <button style = {{position: "absolute", height : "7%", left : "40%", top: "18%"}}
            className={` text-white font-thin py-2 px-4 rounded ${
              props.mode === "summary" ? "bg-gray-700" : ""
            }`}
            onClick={props.onSum}
          >
            Summary
          </button>
          
          <button style = {{position: "absolute", height : "7%", left : "57%", top: "18%"}}
            className={` text-white font-thin py-2 px-4 rounded ${
              props.mode === "info" ? "bg-gray-700" : ""
            }`}
            onClick={props.onInfo}
          >
            Image
          </button>
      <button style = {{position: "absolute", height : "7%", left : "48%", top: "18%"}}
            className={` text-white font-thin py-2 px-4 rounded ${
              props.mode === "ppt" ? "bg-gray-700" : ""
            }`}
            onClick={props.onPpt}
          >
            PowerPoint
          </button>
        </div>
      );
}