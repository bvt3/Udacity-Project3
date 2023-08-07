data "azurerm_resource_group" "image" {
  name                = "${var.image_rg_name}"
}

data "azurerm_image" "image" {
  name                = "${var.image_name}"
  resource_group_name = data.azurerm_resource_group.image.name
}

resource "azurerm_network_interface" "project3" {
  name                = "${var.vm_name}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_availability_set" "availset" {
   name                         = "${var.vm_name}-availset"
   location                     = "${var.location}"
   resource_group_name          = "${var.resource_group}"
   platform_fault_domain_count  = 1
   platform_update_domain_count = 1
   managed                      = true
}

resource "azurerm_virtual_machine" "project3" {
   name                  = "${var.vm_name}"
   location              = "${var.location}"
   availability_set_id   = azurerm_availability_set.availset.id
   resource_group_name   = "${var.resource_group}"
   network_interface_ids = azurerm_network_interface.project3.*.id
   vm_size               = "Standard_B1s"   

   delete_os_disk_on_termination = true
   delete_data_disks_on_termination = true

   storage_image_reference {
     id = "${data.azurerm_image.image.id}"
   }

   storage_os_disk {
     name              = "osdisk"
     caching           = "ReadWrite"
     create_option     = "FromImage"
     managed_disk_type = "Standard_LRS"
   }

   os_profile {
     computer_name  = "${var.computer_name}"
     admin_username = var.admin_user
     admin_password = var.admin_password
   }

   os_profile_linux_config {
     disable_password_authentication = false
   }
 }