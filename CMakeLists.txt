cmake_minimum_required(VERSION 3.30)
project(darkmetal)

# Most of these static libraries have the least dependencies on other modules, and
# with some refactoring they can become even more self-contained
# More importantly, lhnet needs to be fully independent for future online lobby work.

# If we bump the C library version then we can just have a thin wrapper around C11 threads (or use them directly)
# instead of these various wrappers around different backends
add_library(${PROJECT_NAME}-system-shared STATIC 
                        sys_shared.c
                        vid_shared.c                        
                        snd_wav.c
                        snd_ogg.c
                        snd_mem.c
                        snd_mix.c)

add_library(${PROJECT_NAME}-system-win32 EXCLUDE_FROM_ALL STATIC 
                        thread_win.c
                        vid_wgl.c
                        snd_win.c
                        sys_win.c)

add_library(${PROJECT_NAME}-system-linux EXCLUDE_FROM_ALL STATIC 
                        thread_pthread.c
                        vid_glx.c
                        snd_coreaudio.c
                        sys_linux.c)

add_library(${PROJECT_NAME}-system-mac EXCLUDE_FROM_ALL STATIC 
                        thread_pthread.c
                        vid_agl.c
                        snd_coreaudio.c
                        sys_unix.c)

add_library(${PROJECT_NAME}-system-sdl EXCLUDE_FROM_ALL STATIC 
                        thread_sdl.c
                        vid_sdl.c
                        snd_sdl.c
                        sys_sdl.c)

foreach(SYS_TARGET IN ITEMS ${PROJECT_NAME}-system-win32 
                            ${PROJECT_NAME}-system-linux 
                            ${PROJECT_NAME}-system-mac
                            ${PROJECT_NAME}-system-sdl)
    target_link_libraries(${SYS_TARGET} PRIVATE ${PROJECT_NAME}-system-shared)
endforeach()


if (WIN32)
    add_library(${PROJECT_NAME}-system ALIAS ${PROJECT_NAME}-system-win32) 
# TODO add check for SDL package
# TODO add check for UNIX based OSs for pthreads
else()
endif()

add_library(${PROJECT_NAME}-lhnet STATIC lhnet.c)

add_library(${PROJECT_NAME}-math STATIC 
        mathlib.c
        matrixlib.c
        fractalnoise.c
        curves.c)

add_library(${PROJECT_NAME}-renderer-software STATIC dpsoftrast.c)

add_executable(${PROJECT_NAME} WIN32 
        sv_move.c
        sv_main.c
        sv_phys.c
        sv_user.c
        sv_demo.c
        svvm_cmds.c
        cl_main.c
        cl_video.c
        cl_demo.c
        cl_input.c
        cl_parse.c
        cl_particles.c
        cl_collision.c
        cl_dyntexture.c
        cl_video.c
        cl_screen.c
        snd_main.c 
        clvm_cmds.c
        gl_textures.c
        gl_draw.c
        gl_rsurf.c
        gl_rmain.c
        gl_backend.c
        console.c
        r_lightning.c
        r_shadow.c
        r_modules.c
        r_sprites.c
        r_sky.c
        r_explosion.c
        polygon.c
        ft2.c
        bih.c        
        meshqueue.c
        model_shared.c
        model_sprite.c
        model_alias.c
        model_brush.c
        mod_skeletal_animatevertices_sse.c
        mod_skeletal_animatevertices_generic.c        
        cl_parse.c
        csprogs.c
        dpvsimpledecode.c
        builddate.c
        view.c
        sbar.c
        host_cmd.c
        libcurl.c
        collision.c  
        protocol.c 
        netconn.c 
        cap_ogg.c
        svbsp.c
        palette.c
        world.c
        portals.c
        keys.c 
        host.c
        prvm_exec.c
        prvm_cmds.c
        prvm_edict.c
        common.c
        thread_win.c
        zone.c
        image.c
        image_png.c
        utf8lib.c
        fs.c
        cmd.c
        cvar.c
        filematch.c
        zone.c
        wad.c
        mdfour.c
        jpeg.c
        hmac.c
        crypto.c
)

set_target_properties(${PROJECT_NAME} PROPERTIES ENABLE_EXPORTS ON)

target_link_libraries(${PROJECT_NAME} PRIVATE 
        ${PROJECT_NAME}-math        
        ${PROJECT_NAME}-lhnet
        ${PROJECT_NAME}-system
        ${PROJECT_NAME}-renderer-software)