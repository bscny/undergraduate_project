sum_prompt = '''
You are an assistant analyzing a drone video based on detailed descriptions of individual frames, each captured every 3 seconds. I will provide:

1. A set of frame-by-frame scene descriptions, and  
2. A specific instruction (prompt) on how I want the video summarized.

Your task is to generate a video-level summary by strictly following my provided instruction and using only the information from the frame descriptions. Do not use outside knowledge or make assumptions.
'''

merge_prompt = '''
I have two different summaries of a drone video. Use both to understand what happens in the video and generate a new, final summary as if you had watched the video yourself. Focus on describing what is shown in the footage, including key visuals, actions, locations, and any notable events. Don't just summarize the summaries — create a realistic, cohesive description of the video content based on the combined information.
'''