# Local evidence tools

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

`python "<skill-dir>/scripts/transcript_window.py" transcript.json --start 30 --end 90 --limit 100` reads a supplied transcript:

```json
{"identity":"video URL or local source ID","source_coverage":"complete supplied captions","segments":[{"offset":29,"duration":4,"text":"This segment overlaps the requested interval."}]}
```

Segments use seconds. Selection is by overlap with [start,end), including a segment that begins before start but extends into the window. Zero-duration cues use their start time. The helper retains raw text, sorts selected segments, applies the limit last and reports matched/returned counts and truncation. No source identity means identity UNAVAILABLE. Source completeness remains unknown unless supplied; never assume the input contains all captions just because this helper returned all of it.

`python "<skill-dir>/scripts/transcript_window.py" shots.json --pacing` accepts `{"duration":60,"cuts":[10,25]}`. Cuts are distinct ordered internal boundaries, excluding zero and the final duration. It reports two cuts/minute and three shot durations. Sparse selected frames cannot supply a complete cut list. Zero cuts is valid; motion and talking-head measurements are not implemented.

These tools do no downloading, transcription, cookie access or media export. Acquire evidence with available authorized tools. A disabled-transcription choice must remain disabled across every acquisition branch. Clip generation requires a separate actual export tool and inspection of its result.
