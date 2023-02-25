export function SummaryText(props){
    return (
    <div className="bg-gray-800 p-4 rounded-lg" style = {{position : "absolute", top : "30%" ,height : "40%", width: "70%"}}>
    <p className="text-white">{props.summaryText.data.filename}</p>
    </div>
  )
}