import subprocess
import time

#PSNR Testing in x264 condition
def PSNR_264():
    while True:
        print("What parameters would you like to test? 1 for fps, 2 for bit rate, 3 for crf, 4 for voice, 0 for exit")
        p_ch1=int(input())
        if p_ch1==0:
            break
        if p_ch1==1:    #PSNR vs fps
            print("Which one would you like to have a look? 1 for r=1, 2 for r=5, 3 for r=10, 4 for r=20, 5 for r=30")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r1.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r1.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r5.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r5.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r20.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r20.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==5:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r30.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r30.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==0:
                break
        elif p_ch1==2:    #PSNR vs bit rate
            print("Which one would you like to have a look? 1 for b=10k, 2 for b=100k, 3 for b=300k, 4 for b=1M")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-10k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-10k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)

            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-100k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-100k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-1M-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-1M-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
        elif p_ch1==3:    #PSNR vs crf
            print("Which one would you like to have a look? 1 for crf=20, 2 for crf=30, 3 for crf=40, 4 for crf=50")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c20.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c20.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c30.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c30.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c40.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c40.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c50.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c50.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
        elif p_ch1==4:    #PSNR vs voice
            print("Which one would you like to have a look? 1 for human with voice, 2 for human without voice, 3 for object with voice, 4 for object without voice")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h264.mp4 -i box.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h264_an.mp4 -i box.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc.mp4 -i s.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc_an.mp4 -i s.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)









#SSIM Testing in x264 condition
def SSIM_264():
    while True:
        print("What parameters would you like to test? 1 for fps, 2 for bit rate, 3 for crf, 4 for voice, 0 for exit")
        p_ch1=int(input())
        if p_ch1==0:
            break
        if p_ch1==1:    #SSIM vs fps
            print("Which one would you like to have a look? 1 for r=1, 2 for r=5, 3 for r=10, 4 for r=20, 5 for r=30")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r1.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r1.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r5.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r5.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r20.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r20.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==5:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r30.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r30.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==0:
                break
        elif p_ch1==2:    #SSIM vs bit rate
            print("Which one would you like to have a look? 1 for b=10k, 2 for b=100k, 3 for b=300k, 4 for b=1M")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-10k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-10k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-100k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-100k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-1M-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-1M-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
        elif p_ch1==3:    #SSIM vs crf
            print("Which one would you like to have a look? 1 for crf=20, 2 for crf=30, 3 for crf=40, 4 for crf=50")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c20.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c20.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c30.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c30.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c40.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c40.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-264-300k-r10-c50.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-264-300k-r10-c50.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
        elif p_ch1==4:    #SSIM vs voice
            print("Which one would you like to have a look? 1 for human with voice, 2 for human without voice, 3 for object with voice, 4 for object without voice")
            p_ch2=int(input())
            if p_ch2==1:    
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h264.mp4 -i box.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h264_an.mp4 -i box.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc.mp4 -i s.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc_an.mp4 -i s.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)








#VMAF Testing in x264 condition
def VMAF_264():
    while True:
        print("What parameters would you like to test? 1 for fps, 2 for bit rate, 3 for crf, 4 for voice, 0 for exit")
        p_ch1=int(input())
        if p_ch1==0:
            break
        if p_ch1==1:    #VMAF vs fps
            print("Which one would you like to have a look? 1 for r=1, 2 for r=5, 3 for r=10, 4 for r=20, 5 for r=30")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r1.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')

                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r1.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r5.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r5.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r20.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r20.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==5:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r30.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r30.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==0:
                break
        elif p_ch1==2:    #VMAF vs bit rate
            print("Which one would you like to have a look? 1 for b=10k, 2 for b=100k, 3 for b=300k, 4 for b=1M")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-10k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-10k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-100k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-100k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-1M-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-1M-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
        elif p_ch1==3:    #VMAF vs crf
            print("Which one would you like to have a look? 1 for crf=20, 2 for crf=30, 3 for crf=40, 4 for crf=50")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r10-c20.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r10-c20.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r10-c30.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r10-c30.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r10-c40.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r10-c40.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-264-300k-r10-c50.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-264-300k-r10-c50.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
        elif p_ch1==4:    #VMAF vs voice
            print("Which one would you like to have a look? 1 for human with voice, 2 for human without voice, 3 for object with voice, 4 for object without voice")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i box_32_h264.mp4 -i box.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i box_32_h264_an.mp4 -i box.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i s_hevc.mp4 -i s.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i s_hevc_an.mp4 -i s.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)


#PSNR Testing in x265 condition
def PSNR_265():
    while True:
        print("What parameters would you like to test? 1 for fps, 2 for bit rate, 3 for crf, 4 for voice, 0 for exit")
        p_ch1=int(input())
        if p_ch1==0:
            break
        if p_ch1==1:    #PSNR vs fps
            print("Which one would you like to have a look? 1 for r=1, 2 for r=5, 3 for r=10, 4 for r=20, 5 for r=30")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r1.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r1.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r5.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r5.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r20.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r20.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==5:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r30.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r30.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==0:
                break
        elif p_ch1==2:    #PSNR vs bit rate
            print("Which one would you like to have a look? 1 for b=10k, 2 for b=100k, 3 for b=300k, 4 for b=1M")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-10k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-10k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-100k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-100k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-1M-r10.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-1M-r10.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
        elif p_ch1==3:    #PSNR vs crf
            print("Which one would you like to have a look? 1 for crf=20, 2 for crf=30, 3 for crf=40, 4 for crf=50")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c20.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c20.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c30.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c30.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c40.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c40.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c50.mp4 -i a.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c50.mp4 -i c.y4m -lavfi psnr=psnr.log -f null -")
                print(status,output)
        elif p_ch1==4:    #PSNR vs voice
            print("Which one would you like to have a look? 1 for human with voice, 2 for human without voice, 3 for object with voice, 4 for object without voice")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h265.mp4 -i box.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h265_an.mp4 -i box.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc.mp4 -i s.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc_an.mp4 -i s.mp4 -lavfi psnr=psnr.log -f null -")
                print(status,output)









#SSIM Testing in x265 condition
def SSIM_265():
    while True:
        print("What parameters would you like to test? 1 for fps, 2 for bit rate, 3 for crf, 4 for voice, 0 for exit")
        p_ch1=int(input())
        if p_ch1==0:
            break
        if p_ch1==1:    #SSIM vs fps
            print("Which one would you like to have a look? 1 for r=1, 2 for r=5, 3 for r=10, 4 for r=20, 5 for r=30")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r1.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r1.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r5.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r5.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r20.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r20.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==5:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r30.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r30.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==0:
                break
        elif p_ch1==2:    #SSIM vs bit rate
            print("Which one would you like to have a look? 1 for b=10k, 2 for b=100k, 3 for b=300k, 4 for b=1M")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-10k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-10k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-100k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-100k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-1M-r10.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-1M-r10.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
        elif p_ch1==3:    #SSIM vs crf
            print("Which one would you like to have a look? 1 for crf=20, 2 for crf=30, 3 for crf=40, 4 for crf=50")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c20.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c20.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c30.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c30.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c40.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c40.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i a-265-300k-r10-c50.mp4 -i a.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput("ffmpeg -i c-265-300k-r10-c50.mp4 -i c.y4m -lavfi ssim=ssim.log -f null -")
                print(status,output)
        elif p_ch1==4:    #SSIM vs voice
            print("Which one would you like to have a look? 1 for human with voice, 2 for human without voice, 3 for object with voice, 4 for object without voice")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h265.mp4 -i box.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h265_an.mp4 -i box.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc.mp4 -i s.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc_an.mp4 -i s.mp4 -lavfi ssim=ssim.log -f null -")
                print(status,output)








#VMAF Testing in x265 condition
def VMAF_265():
    while True:
        print("What parameters would you like to test? 1 for fps, 2 for bit rate, 3 for crf, 4 for voice, 0 for exit")
        p_ch1=int(input())
        if p_ch1==0:
            break
        if p_ch1==1:    #VMAF vs fps
            print("Which one would you like to have a look? 1 for r=1, 2 for r=5, 3 for r=10, 4 for r=20, 5 for r=30")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r1.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r1.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r5.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r5.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r20.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r20.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==5:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r30.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r30.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==0:
                break
        elif p_ch1==2:    #VMAF vs bit rate
            print("Which one would you like to have a look? 1 for b=10k, 2 for b=100k, 3 for b=300k, 4 for b=1M")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-10k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-10k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-100k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-100k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-1M-r10.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-1M-r10.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
        elif p_ch1==3:    #VMAF vs crf
            print("Which one would you like to have a look? 1 for crf=20, 2 for crf=30, 3 for crf=40, 4 for crf=50")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r10-c20.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r10-c20.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r10-c30.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r10-c30.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r10-c40.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r10-c40.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i a-265-300k-r10-c50.mp4 -i a.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
                print('The result above you have seen is that of human, after few seconds you would see the result of object with same condition')
                time.sleep(5)
                status,output=subprocess.getstatusoutput('./ffmpeg -i c-265-300k-r10-c50.mp4 -i c.y4m -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
        elif p_ch1==4:    #VMAF vs voice
            print("Which one would you like to have a look? 1 for human with voice, 2 for human without voice, 3 for object with voice, 4 for object without voice")
            p_ch2=int(input())
            if p_ch2==1:
                status,output=subprocess.getstatusoutput('./ffmpeg -i box_32_h265.mp4 -i box.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==2:
                status,output=subprocess.getstatusoutput('./ffmpeg -i box_32_h265_an.mp4 -i box.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==3:
                status,output=subprocess.getstatusoutput('./ffmpeg -i s_hevc.mp4 -i s.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)
            elif p_ch2==4:
                status,output=subprocess.getstatusoutput('./ffmpeg -i s_hevc_an.mp4 -i s.mp4 -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                print(status,output)





#Generate all the materials(videos) needed for quality testing
def Generate():
#voice#
    status,output=subprocess.getstatusoutput("ffmpeg -i s_hevc.mp4 -vcodec copy -an s_hevc_an.mp4")
    status,output=subprocess.getstatusoutput("ffmpeg -i box_32_h264.mp4 -vcodec copy -an box_32_h264_an.mp4")

####x264####
##human##
#crf#
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 10 -crf 20 -s 176x144 a-264-300k-r10-c20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 10 -crf 30 -s 176x144 a-264-300k-r10-c30.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 10 -crf 40 -s 176x144 a-264-300k-r10-c40.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 10 -crf 50 -s 176x144 a-264-300k-r10-c50.mp4")
#bit rate#
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 10k -r 10 -s 176x144 a-264-10k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 100k -r 10 -s 176x144 a-264-100k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 10 -s 176x144 a-264-300k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 1M -r 10 -s 176x144 a-264-1M-r10.mp4")
#fps
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 1 -s 176x144 a-264-300k-r1.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 5 -s 176x144 a-264-300k-r5.mp4")
   
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 20 -s 176x144 a-264-300k-r20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx264 -b 300k -r 30 -s 176x144 a-264-300k-r30.mp4")


##object##
#crf#
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 10 -crf 20 -s 176x144 c-264-300k-r10-c20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 10 -crf 30 -s 176x144 c-264-300k-r10-c30.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 10 -crf 40 -s 176x144 c-264-300k-r10-c40.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 10 -crf 50 -s 176x144 c-264-300k-r10-c50.mp4")
#bit rate#
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 10k -r 10 -s 176x144 c-264-10k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 100k -r 10 -s 176x144 c-264-100k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 10 -s 176x144 c-264-300k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 1M -r 10 -s 176x144 c-264-1M-r10.mp4")
#fps
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 1 -s 176x144 c-264-300k-r1.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 5 -s 176x144 c-264-300k-r5.mp4")
    
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 20 -s 176x144 c-264-300k-r20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx264 -b 300k -r 30 -s 176x144 c-264-300k-r30.mp4")

####HEVC####
##human##
#crf#
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 10 -crf 20 -s 176x144 a-265-300k-r10-c20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 10 -crf 30 -s 176x144 a-265-300k-r10-c30.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 10 -crf 40 -s 176x144 a-265-300k-r10-c40.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 10 -crf 50 -s 176x144 a-265-300k-r10-c50.mp4")
    #bit rate#
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 10k -r 10 -s 176x144 a-265-10k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 100k -r 10 -s 176x144 a-265-100k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 10 -s 176x144 a-265-300k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 1M -r 10 -s 176x144 a-265-1M-r10.mp4")
    #fps
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 1 -s 176x144 a-265-300k-r1.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 5 -s 176x144 a-265-300k-r5.mp4")
    
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 20 -s 176x144 a-265-300k-r20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i a.y4m -c libx265 -b 300k -r 30 -s 176x144 a-265-300k-r30.mp4")
    
    
    ##object##
    #crf#
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 10 -crf 20 -s 176x144 c-265-300k-r10-c20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 10 -crf 30 -s 176x144 c-265-300k-r10-c30.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 10 -crf 40 -s 176x144 c-265-300k-r10-c40.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 10 -crf 50 -s 176x144 c-265-300k-r10-c50.mp4")
    #bit rate#
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 10k -r 10 -s 176x144 c-265-10k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 100k -r 10 -s 176x144 c-265-100k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 10 -s 176x144 c-265-300k-r10.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 1M -r 10 -s 176x144 c-265-1M-r10.mp4")
    #fps
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 1 -s 176x144 c-265-300k-r1.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 5 -s 176x144 c-265-300k-r5.mp4")
    
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 20 -s 176x144 c-265-300k-r20.mp4")
    status,output=subprocess.getstatusoutput("./ffmpeg -i c.y4m -c libx265 -b 300k -r 30 -s 176x144 c-265-300k-r30.mp4")


#Plot the figure of quality measurement result 
def figure():
    import numpy as np 
    import matplotlib as mpl 
    import matplotlib.pyplot as plt 



    while True:
        print("Which encoder would you like to test? 1 for x264, 2 for HEVC, 0 for exit")
        f_ch1=int(input())
        if f_ch1==0:
            break
        if f_ch1==1:
            print("Which parameter would you like to have a look? 1 for fps, 2 for bit rate, 3 for crf")
            f_ch2=int(input())
            if f_ch2==1:
                x_axix = [1,5,10,20,30]
                file_size_s = [0.086,0.2668,0.3357,0.348,0.3526]
                psnr_s = [0.3014,0.33809,0.3662,0.38759,0.42957]
                ssim_s = [0.946,0.974,0.985,0.989,0.994]
                vmaf_s = [0.70936,0.84125,0.89565,0.91828,0.94765]
                file_size_d = [0.02398,0.3643,0.3656,0.3645,0.3656]
                psnr_d = [0.1986,0.2208,0.23677,0.24959,0.28355]
                ssim_d = [0.581,0.664,0.743,0.797,0.896]
                vmaf_d = [0.25713,0.3135,0.45218,0.53511,0.7221]
                plt.title('x264--fps') 
                plt.xlabel('fps') 
                plt.plot(x_axix, file_size_s, color='green', label='file_size(/1000)_s') 
                plt.plot(x_axix, file_size_d, color='limegreen', label='file_size(/1000)_d',linestyle=':') 
                plt.plot(x_axix, psnr_s, color='red', label='psnr(/100)_s')
                plt.plot(x_axix, psnr_d, color='brown', label='psnr(/100)_d',linestyle=':') 
                plt.plot(x_axix, ssim_d, color='gold', label='ssim_d',linestyle=':') 
                plt.plot(x_axix, ssim_s, color='yellow', label='ssim_s') 
                plt.plot(x_axix, vmaf_s, color='blue', label='vmaf(/100)_s') 
                plt.plot(x_axix, vmaf_d, color='blueviolet', label='vmaf(/100)_d',linestyle=':')
                plt.legend()  
                plt.ylabel('value') 
                plt.show()
            elif f_ch2==2:     
                x_axix = [10,100,300,1000]
                file_size_s = [0.012,0.1092,0.3357,0.5223]
                psnr_s = [0.3314,0.36516,0.3662,0.3663]
                ssim_s = [0.933,0.983,0.985,0.986]
                vmaf_s = [0.7431,0.89149,0.89565,0.89606]
                file_size_d = [0.0145,0.124,0.3656,1.2]
                psnr_d = [0.23806,0.23778,0.23677,0.23622]
                ssim_d = [0.699,0.747,0.743,0.739]
                vmaf_d = [0.32737,0.44326,0.45218,0.45481]
                plt.title('x264--bit rate') 
                plt.xlabel('bit rate(KB)') 
                plt.plot(x_axix, file_size_s, color='green', label='file_size(/1000)_s') 
                plt.plot(x_axix, file_size_d, color='limegreen', label='file_size(/1000)_d',linestyle=':') 
                plt.plot(x_axix, psnr_s, color='red', label='psnr(/100)_s')
                plt.plot(x_axix, psnr_d, color='brown', label='psnr(/100)_d',linestyle=':') 
                plt.plot(x_axix, ssim_d, color='gold', label='ssim_d',linestyle=':') 
                plt.plot(x_axix, ssim_s, color='yellow', label='ssim_s') 
                plt.plot(x_axix, vmaf_s, color='blue', label='vmaf(/100)_s') 
                plt.plot(x_axix, vmaf_d, color='blueviolet', label='vmaf(/100)_d',linestyle=':')
                plt.legend()  
                plt.ylabel('value') 
                plt.show()
            elif f_ch2==3:     
                x_axix = [20,30,40,50]
                file_size_s = [0.511,0.164,0.076,0.049]
                psnr_s = [0.36412,0.35369,0.32371,0.27858]
                ssim_s = [0.98,0.967,0.925,0.813]
                vmaf_s = [0.8863,0.84769,0.67288,0.29]
                file_size_d = [2.946,0.662,0.148,0.069]
                psnr_d = [0.23694,0.23825,0.23792,0.22581]
                ssim_d = [0.744,0.746,0.7,0.615]
                vmaf_d = [0.451,0.42985,0.33937,0.12843]
                plt.ylim(0,1.1)
                plt.title('x264--crf') 
                plt.xlabel('crf') 
                plt.plot(x_axix, file_size_s, color='green', label='file_size(/100)_s') 
                plt.plot(x_axix, file_size_d, color='limegreen', label='file_size(/100)_d',linestyle=':') 
                plt.plot(x_axix, psnr_s, color='red', label='psnr(/100)_s')
                plt.plot(x_axix, psnr_d, color='brown', label='psnr(/100)_d',linestyle=':') 
                plt.plot(x_axix, ssim_d, color='gold', label='ssim_d',linestyle=':') 
                plt.plot(x_axix, ssim_s, color='yellow', label='ssim_s') 
                plt.plot(x_axix, vmaf_s, color='blue', label='vmaf(/100)_s') 
                plt.plot(x_axix, vmaf_d, color='blueviolet', label='vmaf(/100)_d',linestyle=':')
                plt.legend()  
                plt.ylabel('value') 
                plt.show()

        elif f_ch1==2:
            print("Which parameter would you like to have a look? 1 for fps, 2 for bit rate, 3 for crf")
            f_ch2=int(input())
            if f_ch2==1:
                x_axix = [1,5,10,20,30]
                file_size_s = [0.0838,0.2664,0.3349,0.3503,0.3524]
                psnr_s = [0.3014,0.3382,0.36634,0.38799,0.43083]
                ssim_s = [0.946,0.974,0.985,0.989,0.994]
                vmaf_s = [0.70995,0.84160,0.89612,0.91924,0.94848]
                file_size_d = [0.0236,0.4646,0.3911,0.3684,0.3646]
                psnr_d = [0.1987,0.2209,0.23691,0.24994,0.28391]
                ssim_d = [0.581,0.664,0.743,0.8,0.899]
                vmaf_d = [0.25775,0.31346,0.45293,0.53847,0.72353]
                plt.title('HEVC--fps') 
                plt.xlabel('fps') 
                plt.plot(x_axix, file_size_s, color='green', label='file_size(/1000)_s') 
                plt.plot(x_axix, file_size_d, color='limegreen', label='file_size(/1000)_d',linestyle=':') 
                plt.plot(x_axix, psnr_s, color='red', label='psnr(/100)_s')
                plt.plot(x_axix, psnr_d, color='brown', label='psnr(/100)_d',linestyle=':') 
                plt.plot(x_axix, ssim_d, color='gold', label='ssim_d',linestyle=':') 
                plt.plot(x_axix, ssim_s, color='yellow', label='ssim_s') 
                plt.plot(x_axix, vmaf_s, color='blue', label='vmaf(/100)_s') 
                plt.plot(x_axix, vmaf_d, color='blueviolet', label='vmaf(/100)_d',linestyle=':')
                plt.legend()  
                plt.ylabel('value') 
                plt.show()
            elif f_ch2==2:     
                x_axix = [10,100,300,1000]
                file_size_s = [0.0157,0.115,0.3349,0.492]
                psnr_s = [0.348,0.36516,0.36634,0.36641]
                ssim_s = [0.959,0.983,0.985,0.986]
                vmaf_s = [0.82423,0.89418,0.89612,0.89617]
                file_size_d = [0.0171,0.129,0.3911,1.3]
                psnr_d = [0.23856,0.23802,0.23691,0.23631]
                ssim_d = [0.711,0.749,0.745,0.739]
                vmaf_d = [0.34078,0.44296,0.45294,0.45478]
                plt.title('HEVC--bit rate') 
                plt.xlabel('bit rate(KB)') 
                plt.plot(x_axix, file_size_s, color='green', label='file_size(/1000)_s') 
                plt.plot(x_axix, file_size_d, color='limegreen', label='file_size(/1000)_d',linestyle=':') 
                plt.plot(x_axix, psnr_s, color='red', label='psnr(/100)_s')
                plt.plot(x_axix, psnr_d, color='brown', label='psnr(/100)_d',linestyle=':') 
                plt.plot(x_axix, ssim_d, color='gold', label='ssim_d',linestyle=':') 
                plt.plot(x_axix, ssim_s, color='yellow', label='ssim_s') 
                plt.plot(x_axix, vmaf_s, color='blue', label='vmaf(/100)_s') 
                plt.plot(x_axix, vmaf_d, color='blueviolet', label='vmaf(/100)_d',linestyle=':')
                plt.legend()  
                plt.ylabel('value') 
                plt.show()
            elif f_ch2==3:     
                x_axix = [20,30,40,50]
                file_size_s = [0.577,0.214,0.1,0.075]
                psnr_s = [0.36481,0.35687,0.33038,0.2877]
                ssim_s = [0.98,0.971,0.932,0.831]
                vmaf_s = [0.889,0.857,0.72954,0.413]
                file_size_d = [3.225,0.878,0.207,0.084]
                psnr_d = [0.23707,0.23845,0.23963,0.23113]
                ssim_d = [0.746,0.749,0.721,0.63]
                vmaf_d = [0.45229,0.43806,0.36623,0.12334]
                plt.ylim(0,1.1)
                plt.title('HEVC--crf') 
                plt.xlabel('crf') 
                plt.plot(x_axix, file_size_s, color='green', label='file_size(/100)_s') 
                plt.plot(x_axix, file_size_d, color='limegreen', label='file_size(/100)_d',linestyle=':') 
                plt.plot(x_axix, psnr_s, color='red', label='psnr(/100)_s')
                plt.plot(x_axix, psnr_d, color='brown', label='psnr(/100)_d',linestyle=':') 
                plt.plot(x_axix, ssim_d, color='gold', label='ssim_d',linestyle=':') 
                plt.plot(x_axix, ssim_s, color='yellow', label='ssim_s') 
                plt.plot(x_axix, vmaf_s, color='blue', label='vmaf(/100)_s') 
                plt.plot(x_axix, vmaf_d, color='blueviolet', label='vmaf(/100)_d',linestyle=':')
                plt.legend()  
                plt.ylabel('value') 
                plt.show()





#Main Function
if __name__=='__main__':
    while True:
        print("Welcome to the video quality test bed, if you are new to this testing system, please press 1 to allow relevant videos be generated, which would take a few seconds, or press 2 to start the testing directly if you have already generated them: ")
        num=int(input())
        if num==1:
            Generate()
            print("All of the videos have been generated successfully, thank you for your patience!")
        elif num==2: 
            break
          
while True:
    print("Please choose the measurement of two different encoding tools: 1 for x264, 2 for HEVC, 0 for exit or if you would like to see the figure of result, press 3")
    ch0=int(input())
    if ch0==0:
        break
    if ch0==3:
        figure()    
    if ch0==1: 
        while True:
            print("Please choose the quality factor you want to examine. 1 for PSNR, 2 for SSIM, 3 for VMAF, 0 for exit")
            ch1=int(input())
            if ch1==1:
                PSNR_264()
            elif ch1==2:
                SSIM_264()
            elif ch1==3:
                VMAF_264()
            elif ch1==0:
                break
            else:
                print("Please insert the correct choice!")
    elif ch0==2:
        while True:
            print("Please choose the quality factor you want to examine. 1 for PSNR, 2 for SSIM, 3 for VMAF, 0 for exit")
            ch1=int(input())
            if ch1==1:
                PSNR_265()
            elif ch1==2:
                SSIM_265()
            elif ch1==3:
                VMAF_265()
            elif ch1==0:
                    break
            else:
                print("Please insert the correct choice!")
