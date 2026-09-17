# Video evidence procedure

## Captions and timing

Keep the original video ID or URL, timestamp origin, language, and whether the transcript is manual or automatically generated. Parse VTT/SRT timestamps rather than estimating time from word position. Mark uncertain names, speaker changes, or transcription errors when they affect the answer. Missing captions do not prove silence.

A transcript saying that a demonstration is accelerated does not establish whether its measurements are valid. Say the available evidence does not verify the claim; do not conclude that unseen footage could never support it. A visible clock, test log, or other measurement might supply evidence that the transcript omits.

## Frames

Use a native video tool when present. Otherwise discover local ffprobe/ffmpeg or equivalent tools and check their actual help before generating commands. Use explicit argument lists, quoted literal paths, a task-specific output directory, and no overwriting of the source media. Probe duration first so seeks remain inside the file.

For a general visual summary, select representative scenes and cover the requested interval. Increase density near an event or transition that matters to the question. For a hook critique, inspect the opening interval closely and compare its visuals with the words and on-screen text. Keep a manifest of frame filename and actual timestamp. Sampling is incomplete coverage; do not infer an unseen event never happened.

Cuts-per-minute requires detected or inspected cut times and a known interval: count cuts divided by interval minutes. Do not use the number of uniformly extracted frames as the cut count. Describe sparse impressions qualitatively when precise measurement is unavailable.

## Fallbacks and stopping

- Transcript supplied without a video ID or URL: identify it as the user-supplied transcript, retain its timestamps, and mark the video identity unavailable. Do not invent a title, channel, or link; request the source only if the task needs identification or visual verification.
- No video access, but a transcript exists: answer spoken-content questions and label the visual portion unverified.
- Frames exist without audio: describe what was observed and mark spoken content unavailable.
- Only metadata exists: report metadata or search leads, not a substantive summary of unseen content.
- A missing tool blocks a requested media artifact: finish the supported research and name the exact missing capability. Do not cite a nonexistent bundled helper.
- A download or remote service fails: make a bounded retry if appropriate, then switch to an available permitted source or state the gap. Do not repeatedly bypass authentication challenges.

For an exported clip, verify that it opens, covers the requested interval, and preserves the requested audio/video streams. Keyframe-aligned cuts may not be exact; inspect boundaries before claiming precise timing.
