export function Language(props){
    return (
        <div className="relative inline-block" style={{position:"absolute", top: "7.5%", left: "89%"}}>
          <select
            className="text-white block appearance-none w-full bg-gray-700 border border-gray-800 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
            value={props.selectedLanguage.value}
            onChange={props.handleLanguageChange}
          >
            {props.languageOptions.map(option => (
              <option key={option.value} value={option.value}>{option.label}</option>
            ))}
          </select>
          <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-white">
            <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 12l-5-5 1.41-1.41L10 9.18l3.59-3.59L15 7l-5 5z"/></svg>
          </div>
        </div>
      );
}