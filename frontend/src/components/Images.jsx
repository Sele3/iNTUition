export function Images(){
    const images = require.context("../../public/images", true);
    const imageFilenames = images.keys();

    const imagesData = imageFilenames.map(filename => {
    const src = images(filename);
    const alt = filename.replace('./', '').replace(/\.[^/.]+$/, ''); return {
        src,
        alt,
        };
    });
    
    return(
        <div className="bg-gray-800 p-4 rounded-lg" style={{ position: "absolute", top: "30%", height: "fit-content", width: "100%", overflowX: "auto" }}>
  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4" style={{ display: "flex", flexDirection: "row", flexWrap: "nowrap", justifyContent: "flex-start", alignItems: "center" }}>
    {imagesData.map((image) => (
      <div key={image.src} style={{ minWidth: "60%", maxWidth: "60%", height: "auto" }}>
        <img src={image.src} alt={image.alt} style={{ height: "60%", width: "60%", objectFit: "cover" }} />
      </div>
    ))}
  </div>
</div>

    )
}