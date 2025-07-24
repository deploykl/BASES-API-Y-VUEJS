import { defineStore } from "pinia";
import { ref, computed } from "vue";
import defaultAvatar from "@/assets/img/header/default-avatar.png";
import { api } from "@/components/services/Axios";
import { toast } from 'vue-sonner';

export const useUserStore = defineStore("user", () => {
  const userData = ref({
    username: "",
    email: "",
    first_name: "",
    last_name: "",
    image: "",
  });

  const imageError = ref(false);
  const loading = ref(false);

  const effectiveUserImage = computed(() => {
    if (imageError.value || !userData.value.image) return defaultAvatar;

    // Si es una imagen en base64 (vista previa), devolver directamente
    if (userData.value.image.startsWith("data:")) {
      return userData.value.image;
    }

    // Añadir parámetro de caché único para imágenes remotas
    const cacheBuster = `?t=${Date.now()}`;

    if (userData.value.image.startsWith("http")) {
      return `${userData.value.image}${cacheBuster}`;
    }

    if (!userData.value.image.startsWith("/media/")) {
      return `${process.env.VUE_APP_IMG_SERVER}media/${userData.value.image}${cacheBuster}`;
    }

    return `${process.env.VUE_APP_IMG_SERVER}${userData.value.image.replace(/^\/+/, "")}${cacheBuster}`;
  });
  
  const fullName = computed(() =>
    `${userData.value.first_name} ${userData.value.last_name}`.trim()
  );

  async function fetchUserProfile() {
    const accessToken = localStorage.getItem("auth_token");
    if (!accessToken) return null;

    loading.value = true;
    try {
      const response = await api.get("user/profile/", {
        headers: { Authorization: `Bearer ${accessToken}` },
      });
      
      updateUserData(response.data);
      imageError.value = false;
      return response.data;
    } catch (error) {
      console.error("Error al obtener perfil:", error);
      imageError.value = true;
      throw error;
    } finally {
      loading.value = false;
    }
  }

  function updateUserData(newData) {
    userData.value = {
      ...userData.value,
      ...newData,
      // Solo añadir timestamp si no es una imagen en base64
      image: newData.image 
        ? newData.image.startsWith("data:") 
          ? newData.image 
          : `${newData.image}?${Date.now()}`
        : ""
    };
  }

  function setImageError(value) {
    imageError.value = value;
  }

  async function updateUserProfile(selectedImage) {
    loading.value = true;

    try {
      const formData = new FormData();
      formData.append('username', userData.value.username);
      formData.append('email', userData.value.email);
      formData.append('first_name', userData.value.first_name);
      formData.append('last_name', userData.value.last_name);

      if (selectedImage) {
        formData.append('image', selectedImage);
      }

      const response = await api.put('user/profile/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
        }
      });

      this.updateUserData({
        ...response.data,
        image: response.data.image ? `${response.data.image}?t=${Date.now()}` : ''
      });

      await this.fetchUserProfile();
      toast.success('Perfil actualizado correctamente');
      return true;
    } catch (error) {
      console.error('Error al actualizar perfil:', error);
      const errorData = error.response?.data || {};
      const errorMessage = errorData.username 
        || errorData.email 
        || errorData.detail 
        || 'Error al actualizar el perfil';
      toast.error(errorMessage);
      return false;
    } finally {
      loading.value = false;
    }
  }

  return {
    userData,
    imageError,
    loading,
    effectiveUserImage,
    fullName,
    fetchUserProfile,
    updateUserData,
    setImageError,
    updateUserProfile
  };
});