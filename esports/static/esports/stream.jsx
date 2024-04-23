import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const Stream = () => {
    const openStream = (event) => {
        event.preventDefault();
        const streamURL = event.target.href;
        window.open(streamURL, '_blank');
    };

    return (
        <div>
            <h2>Streams</h2>
            <ul className="midcol">
                <li>
                    <a href="https://www.twitch.tv/jynxzi" onClick={openStream}>Jynxzi's Twitch Stream</a>
                </li>
                <li>
                    <a href="https://www.youtube.com/c/kaicenat" onClick={openStream}>KaiceNat's YouTube Channel</a>
                </li>
                {/* Add more stream links as needed */}
            </ul>
        </div>
    );
};


function VideoList({ videos, emptyHeading }) {
    const count = videos.length;
    let heading = emptyHeading;
    if (count > 0) {
      const noun = count > 1 ? 'Videos' : 'Video';
      heading = count + ' ' + noun;
    }
    return (
      <section>
        <h2>{heading}</h2>
        {videos.map(video =>
          <Video key={video.id} video={video} />
        )}
      </section>
    );
  }

export default Stream;

